import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from .core import MetadataManager

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MetaExif Pro | Universal Metadata Editor")
        self.geometry("900x600")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        # Set Icon
        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass # Linux/Mac often handle icons differently or fail on .ico bitmaps

        self.files = []
        self.current_idx = None

        self._setup_ui()

    def _setup_ui(self):
        # Layout: Grid 1x2
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # LEFT SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(2, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="MetaExif Pro", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_add_files = ctk.CTkButton(self.sidebar, text="Add Files", command=self.add_files)
        self.btn_add_files.grid(row=1, column=0, padx=20, pady=10)

        # File List
        self.scroll_files = ctk.CTkScrollableFrame(self.sidebar, label_text="Files")
        self.scroll_files.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # RIGHT EDITOR
        self.editor = ctk.CTkFrame(self)
        self.editor.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.lbl_info = ctk.CTkLabel(self.editor, text="Select a file to edit", font=ctk.CTkFont(size=16))
        self.lbl_info.pack(pady=10)

        # Dynamic Fields Area
        self.fields_container = ctk.CTkScrollableFrame(self.editor, label_text="Metadata Tags")
        self.fields_container.pack(fill="both", expand=True, padx=20, pady=10)

        self.rows = [] # List of (key_entry, value_entry, frame) tuples

        # Controls
        self.controls = ctk.CTkFrame(self.editor, fg_color="transparent")
        self.controls.pack(fill="x", padx=20, pady=10)

        self.btn_add_row = ctk.CTkButton(self.controls, text="+ Add Tag", command=self.add_empty_row, width=100)
        self.btn_add_row.pack(side="left", padx=5)

        self.btn_fake = ctk.CTkButton(self.controls, text="🪄 Auto-Fake", command=self.open_preset_dialog, width=100, fg_color="purple")
        self.btn_fake.pack(side="left", padx=5)

        self.btn_save = ctk.CTkButton(self.controls, text="Save Changes", command=self.save_metadata, fg_color="green", width=100)
        self.btn_save.pack(side="right", padx=5)
        
        # Status
        self.status = ctk.CTkLabel(self.editor, text="Ready", text_color="gray")
        self.status.pack(side="bottom", pady=5)

    def add_files(self):
        paths = filedialog.askopenfilenames()
        new_files = []
        for p in paths:
            if p not in self.files:
                self.files.append(p)
                self._add_file_item(p)
                new_files.append(p)
        
        # Auto-select the first file if nothing is selected
        if new_files and self.current_idx is None:
            self.load_file(new_files[0])

    def _add_file_item(self, path):
        name = os.path.basename(path)
        btn = ctk.CTkButton(self.scroll_files, text=name, fg_color="transparent", border_width=1,
                            command=lambda p=path: self.load_file(p))
        btn.pack(fill="x", pady=2)

    def load_file(self, path):
        self.current_idx = path
        self.lbl_info.configure(text=os.path.basename(path))
        
        # Clear existing rows
        for r in self.rows:
            r[2].destroy()
        self.rows.clear()
        
        meta = MetadataManager.load(path)
        
        # Sort keys for better UX
        sorted_keys = sorted(meta.keys())
        for k in sorted_keys:
            self.add_row(k, meta[k])

        if not sorted_keys:
             self.status.configure(text=f"Loaded {os.path.basename(path)} (No tags found)")
        else:
             self.status.configure(text=f"Loaded {os.path.basename(path)}")

    def add_empty_row(self):
        self.add_row("", "")

    def add_row(self, key, value):
        row_frame = ctk.CTkFrame(self.fields_container, fg_color="transparent")
        row_frame.pack(fill="x", pady=2)
        
        # Key Entry
        k_entry = ctk.CTkEntry(row_frame, width=150, placeholder_text="Key")
        k_entry.insert(0, str(key))
        k_entry.pack(side="left", padx=(0, 5))
        
        # Value Entry
        v_entry = ctk.CTkEntry(row_frame, placeholder_text="Value")
        v_entry.insert(0, str(value))
        v_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        # Mark read-only fields as disabled (can't be changed by metadata editing)
        readonly_keys = ["File:Size", "@Resolution", "@Format", "@Mode", "@Frames", "@Duration", "@Bitrate", "@SampleRate", "@Channels", "@Encoder", "@Pages"]
        if key.startswith("@") or key in readonly_keys:
            v_entry.configure(state="disabled", fg_color="#1a1a1a", text_color="gray")
            k_entry.configure(state="disabled", fg_color="#1a1a1a", text_color="gray")
        
        # Delete Button
        btn_del = ctk.CTkButton(row_frame, text="X", width=30, fg_color="red", 
                                command=lambda f=row_frame: self.delete_row(f))
        btn_del.pack(side="right")
        
        self.rows.append((k_entry, v_entry, row_frame))

    def delete_row(self, frame):
        # Remove from list
        self.rows = [r for r in self.rows if r[2] != frame]
        frame.destroy()

    def open_preset_dialog(self):
        from .presets import PRESETS
        
        dialog = ctk.CTkToplevel(self)
        dialog.title("Select Device Preset")
        dialog.geometry("300x400")
        dialog.transient(self) # Make it modal-like on top
        
        lbl = ctk.CTkLabel(dialog, text="Choose a device profile to mimic:", font=("Arial", 14, "bold"))
        lbl.pack(pady=10)
        
        scroll = ctk.CTkScrollableFrame(dialog)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        for name in PRESETS.keys():
            btn = ctk.CTkButton(scroll, text=name, command=lambda n=name: [self.apply_preset(n), dialog.destroy()])
            btn.pack(fill="x", pady=5)

    def apply_preset(self, preset_name):
        from .presets import PRESETS, generate_filename
        if preset_name not in PRESETS: return
        
        # 0. CLEAN TRACES - Remove Windows "downloaded from internet" marker
        try:
            zone_id_path = self.current_idx + ":Zone.Identifier"
            if os.path.exists(zone_id_path):
                os.remove(zone_id_path)
                print("[Mimicry] Removed Zone.Identifier (download trace)")
        except:
            pass  # Not all systems support ADS removal this way
        
        # 1. Rename the file
        try:
            current_path = self.current_idx
            directory = os.path.dirname(current_path)
            _, ext = os.path.splitext(current_path)
            
            new_name = generate_filename(preset_name, ext)
            new_path = os.path.join(directory, new_name)
            
            # Avoid overwriting
            if os.path.exists(new_path):
                 # Fail gracefully or append random? Appending random is safer for fake generation
                 base, ext = os.path.splitext(new_name)
                 new_path = os.path.join(directory, f"{base}_{random.randint(10,99)}{ext}")

            os.rename(current_path, new_path)
            
            # Update Internal State
            if current_path in self.files:
                self.files[self.files.index(current_path)] = new_path
            self.current_idx = new_path
            
            # Update UI List
            for widget in self.scroll_files.winfo_children():
                 # Finding the button by checking its command bound value is hard with lambda
                 # Relying on text match (unsafe if duplicates) or just reloading list completely
                 # Simplest: Update text if it matches old name
                 if widget.cget("text") == os.path.basename(current_path):
                     widget.configure(text=os.path.basename(new_path))
                     widget.configure(command=lambda p=new_path: self.load_file(p))
            
            self.lbl_info.configure(text=os.path.basename(new_path))

        except Exception as e:
            messagebox.showerror("Rename Error", f"Could not rename file: {e}")
            return # Don't continue to metadata if file is lost

        # 2. Apply Metadata
        new_data = PRESETS[preset_name]()
        existing_keys = {}
        for idx, (k_entry, v_entry, _) in enumerate(self.rows):
             existing_keys[k_entry.get().strip()] = v_entry
        
        for k, v in new_data.items():
            if k in existing_keys:
                existing_keys[k].delete(0, "end")
                existing_keys[k].insert(0, str(v))
                existing_keys[k].configure(fg_color="#2B2B2B") # Highlight change
            else:
                self.add_row(k, v)
        
        # Update File:Path display if present
        if "File:Path" in existing_keys:
            existing_keys["File:Path"].delete(0, "end")
            existing_keys["File:Path"].insert(0, new_path)

        self.status.configure(text=f"Applying {preset_name}...")
        
        # AUTO-SAVE immediately after applying preset
        self.save_metadata()
        
        messagebox.showinfo("Mimicry Complete", f"File: {os.path.basename(new_path)}\nDevice: {preset_name}\nAll metadata written to disk!")

    def save_metadata(self):
        if not self.current_idx:
            return

        data = {}
        for k_entry, v_entry, _ in self.rows:
            k = k_entry.get().strip()
            v = v_entry.get().strip()
            if k:
                data[k] = v
        
        # Check if File:Path changed (user wants to rename/move)
        new_path = data.get("File:Path", "").strip()
        current_path = self.current_idx
        
        if new_path and new_path != current_path:
            try:
                # Rename/Move the file
                os.rename(current_path, new_path)
                print(f"[UI] File renamed: {current_path} -> {new_path}")
                
                # Update internal state
                if current_path in self.files:
                    self.files[self.files.index(current_path)] = new_path
                self.current_idx = new_path
                current_path = new_path
                
                # Update sidebar button
                for widget in self.scroll_files.winfo_children():
                    if hasattr(widget, 'cget') and widget.cget("text") == os.path.basename(self.current_idx):
                        pass  # Already correct
                    elif hasattr(widget, 'cget'):
                        # Try to find and update
                        try:
                            widget.configure(text=os.path.basename(new_path))
                            widget.configure(command=lambda p=new_path: self.load_file(p))
                        except:
                            pass
                            
            except Exception as e:
                messagebox.showerror("Rename Failed", f"Could not rename file: {e}")
                return
        
        # Save metadata to the (possibly new) file
        MetadataManager.save(current_path, data)
        
        # Reload file to show ACTUAL saved data
        self.load_file(current_path)
        
        self.status.configure(text=f"Saved & Reloaded: {os.path.basename(current_path)}")
        messagebox.showinfo("Success", "Metadata saved! Reloaded from disk.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
