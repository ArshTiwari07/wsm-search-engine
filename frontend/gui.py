import tkinter as tk
from tkinter import ttk


class SearchGUI:
    BG = '#0B1020'
    PANEL = '#151D30'
    CARD = '#1B263B'
    TEXT = '#F1F5F9'
    MUTED = '#94A3B8'
    ACCENT = '#528BFF'
    BORDER = '#2A3952'

    def __init__(self, search_function):
        self.search_function = search_function
        self.root = tk.Tk()
        self.root.title('Indexly | WSM Search Engine')
        self.root.geometry('960x680')
        self.root.minsize(700, 500)
        self.root.configure(bg=self.BG)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Vertical.TScrollbar', background=self.CARD,
                        troughcolor=self.BG, bordercolor=self.BG,
                        arrowcolor=self.MUTED)

        outer = tk.Frame(self.root, bg=self.BG)
        outer.pack(fill='both', expand=True, padx=42, pady=28)

        header = tk.Frame(outer, bg=self.BG)
        header.pack(fill='x')
        tk.Label(header, text='◈', bg=self.BG, fg=self.ACCENT,
                 font=('Segoe UI', 25, 'bold')).pack(side='left')
        tk.Label(header, text='  Indexly', bg=self.BG, fg=self.TEXT,
                 font=('Segoe UI', 22, 'bold')).pack(side='left')
        tk.Label(header, text='WSM  /  DOCUMENT SEARCH', bg=self.BG,
                 fg=self.MUTED, font=('Segoe UI', 10)).pack(side='right')

        tk.Label(outer, text='Find what matters.', bg=self.BG, fg=self.TEXT,
                 font=('Segoe UI', 30, 'bold')).pack(anchor='w', pady=(42, 5))
        tk.Label(outer, text='Search your document collection instantly with keywords and wildcards.',
                 bg=self.BG, fg=self.MUTED, font=('Segoe UI', 11)).pack(anchor='w')

        search_panel = tk.Frame(outer, bg=self.PANEL, highlightbackground=self.BORDER,
                                highlightthickness=1)
        search_panel.pack(fill='x', pady=(25, 12), ipady=12, ipadx=12)
        tk.Label(search_panel, text='⌕', bg=self.PANEL, fg=self.ACCENT,
                 font=('Segoe UI', 24)).pack(side='left', padx=(10, 8))
        self.search_entry = tk.Entry(search_panel, bg=self.PANEL, fg=self.TEXT,
                                     insertbackground=self.TEXT, relief='flat',
                                     font=('Segoe UI', 14), borderwidth=0)
        self.search_entry.pack(side='left', fill='x', expand=True, ipady=7)
        self.search_entry.insert(0, '')
        self.search_entry.bind('<Return>', lambda _event: self.search())
        tk.Button(search_panel, text='Search  →', command=self.search,
                  bg=self.ACCENT, fg='#FFFFFF', activebackground='#3D73DE',
                  activeforeground='#FFFFFF', relief='flat', cursor='hand2',
                  font=('Segoe UI', 11, 'bold'), padx=22, pady=11,
                  borderwidth=0).pack(side='right', padx=(12, 4))

        chips = tk.Frame(outer, bg=self.BG)
        chips.pack(fill='x', pady=(0, 25))
        tk.Label(chips, text='TRY:', bg=self.BG, fg=self.MUTED,
                 font=('Segoe UI', 9, 'bold')).pack(side='left', padx=(0, 12))
        for term in ('python', 'machine learning', 'pro*', 'j?va'):
            tk.Button(chips, text=term, command=lambda q=term: self.search_for(q),
                      bg=self.CARD, fg='#C8D7F5', activebackground=self.BORDER,
                      activeforeground=self.TEXT, relief='flat', cursor='hand2',
                      font=('Segoe UI', 10), padx=12, pady=6).pack(side='left', padx=(0, 9))

        results_header = tk.Frame(outer, bg=self.BG)
        results_header.pack(fill='x', pady=(0, 12))
        tk.Label(results_header, text='Search results', bg=self.BG, fg=self.TEXT,
                 font=('Segoe UI', 16, 'bold')).pack(side='left')
        self.count_label = tk.Label(results_header, text='Ready to search',
                                    bg=self.BG, fg=self.MUTED, font=('Segoe UI', 10))
        self.count_label.pack(side='right')

        results_border = tk.Frame(outer, bg=self.BORDER, padx=1, pady=1)
        results_border.pack(fill='both', expand=True)
        results_container = tk.Frame(results_border, bg=self.PANEL)
        results_container.pack(fill='both', expand=True)
        self.canvas = tk.Canvas(results_container, bg=self.PANEL, highlightthickness=0)
        scrollbar = ttk.Scrollbar(results_container, orient='vertical', command=self.canvas.yview)
        self.result_frame = tk.Frame(self.canvas, bg=self.PANEL)
        self.window_id = self.canvas.create_window((0, 0), window=self.result_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        self.result_frame.bind('<Configure>', lambda _e: self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfigure(
            self.window_id, width=e.width))
        self.show_empty('Your results will appear here',
                        'Enter a keyword or try a wildcard query to get started.')

        footer = tk.Frame(outer, bg=self.BG)
        footer.pack(fill='x', pady=(16, 0))
        tk.Label(footer, text='●  LOCAL SEARCH ENGINE', bg=self.BG,
                 fg='#5FCA9D', font=('Segoe UI', 9, 'bold')).pack(side='left')
        tk.Label(footer, text='Supports AND search  •  * and ? wildcards',
                 bg=self.BG, fg=self.MUTED, font=('Segoe UI', 9)).pack(side='right')
        self.search_entry.focus_set()

    def clear_results(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        self.canvas.yview_moveto(0)

    def show_empty(self, title, subtitle):
        self.clear_results()
        tk.Label(self.result_frame, text='⌕', bg=self.PANEL, fg=self.ACCENT,
                 font=('Segoe UI', 38)).pack(pady=(65, 4))
        tk.Label(self.result_frame, text=title, bg=self.PANEL, fg=self.TEXT,
                 font=('Segoe UI', 15, 'bold')).pack()
        tk.Label(self.result_frame, text=subtitle, bg=self.PANEL, fg=self.MUTED,
                 font=('Segoe UI', 10), wraplength=500).pack(pady=(8, 55))

    def search_for(self, query):
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, query)
        self.search()

    def search(self):
        query = self.search_entry.get().strip()
        if not query:
            self.count_label.config(text='Ready to search')
            self.show_empty('Enter a search query', 'Type a word or choose an example above.')
            return
        try:
            results = self.search_function(query)
        except Exception as exc:
            self.count_label.config(text='Search error')
            self.show_empty('Something went wrong', str(exc))
            return

        self.clear_results()
        self.count_label.config(text=f'{len(results)} document(s) found')
        if not results:
            self.show_empty('No documents found', 'Try another keyword or a wildcard such as pro*.')
            return

        for number, filename in enumerate(results, 1):
            card = tk.Frame(self.result_frame, bg=self.CARD,
                            highlightbackground=self.BORDER, highlightthickness=1)
            card.pack(fill='x', padx=16, pady=(14, 0))
            tk.Label(card, text='▤', bg=self.CARD, fg=self.ACCENT,
                     font=('Segoe UI', 22)).pack(side='left', padx=(18, 14), pady=17)
            info = tk.Frame(card, bg=self.CARD)
            info.pack(side='left', fill='both', expand=True, pady=14)
            tk.Label(info, text=filename, bg=self.CARD, fg=self.TEXT,
                     font=('Segoe UI', 12, 'bold'), anchor='w').pack(fill='x')
            tk.Label(info, text=f'Document #{number}  •  Keyword match',
                     bg=self.CARD, fg=self.MUTED,
                     font=('Segoe UI', 9), anchor='w').pack(fill='x', pady=(5, 0))
            tk.Label(card, text='MATCH', bg=self.CARD, fg='#5FCA9D',
                     font=('Segoe UI', 9, 'bold')).pack(side='right', padx=20)

    def run(self):
        self.root.mainloop()
