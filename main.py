
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from Bio import SeqIO


class BioPythonProject:

    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("FASTA files", "*.fasta"), ("all files", "*.*")))
        if filename:
            self.file_label.config(text=filename,background="#DBDEF8")

    def select_record(self):
        record_id = self.record_entry.get()

        for record in SeqIO.parse(self.file_label['text'], 'fasta'):
            if record.id == record_id or record.name == record_id:
                gc_content = round((record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100, 2)

                reverse_complement = str(record.seq.reverse_complement())

                rna_sequence = str(record.seq.transcribe())

                self.gc_label.config(text=f"GC Content: {gc_content}%")
                self.rc_label.config(text=f"Reverse complement: {reverse_complement}")
                self.rna_label.config(text=f"RNA sequence: {rna_sequence}")
                break
        else:
            self.gc_label.config(text="")
            self.rc_label.config(text="")
            self.rna_label.config(text="")
            self.status_label.config(text="Record not found")

    def modify_id(self):
        record_id = self.record_entry.get()
        for record in SeqIO.parse(self.file_label['text'], 'fasta'):
            if record.id == record_id or record.name == record_id:
                new_id = tk.simpledialog.askstring("Modify ID", f"Enter new ID for {record_id}")
                if new_id:
                    record.id = new_id
                    record.description = ''
                    SeqIO.write(record, self.file_label['text'], 'fasta')
                    self.status_label.config(text=f"Record ID modified to {new_id}")
                break
        else:
            self.status_label.config(text="Record not found")

    def __init__(self, master):
        self.master = master
        self.master.title("Bio Python Project")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", foreground="#0D165D", background="#DBDEF8",heigth=100, width=200,  radius=25   )
        style.configure("TButton", foreground="white", background="#0D165D",radius=25)
        style.configure("TEntry", foreground="#0D165D", background="#DBDEF8",radius=25),
        self.browse_button = ttk.Button(self.master, text="Browse", command=self.browse_file, )
        self.file_label = ttk.Label(self.master)
        self.record_entry = ttk.Entry(self.master)
        self.select_button = ttk.Button(self.master, text="Select record", command=self.select_record, padding=10)
        self.gc_label = ttk.Label(self.master)
        self.rc_label = ttk.Label(self.master)
        self.rna_label = ttk.Label(self.master)
        self.modify_button = ttk.Button(self.master, text="Modify ID", command=self.modify_id, padding=10)
        self.status_label = ttk.Label(self.master)
        self.browse_button.grid(row=0, column=1, padx=10, pady=10,)
        self.file_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.record_entry.grid(row=1, column=0, sticky="nsew ", padx=10, pady=10)
        self.select_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.gc_label.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.rc_label.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.rna_label.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)
        self.modify_button.grid(row=5, column=1, sticky="nsew", padx=10, pady=10)
        self.status_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)


if __name__ == "__main__":
    main = tk.Tk()
    app = BioPythonProject(main)
    main.mainloop()