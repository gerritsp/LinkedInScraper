class Paper:

    def __init__(self, title, summary, pdf_url, authors):
        self.title = title
        self.summary = summary
        self.pdf_url = pdf_url
        self.authors = authors

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Authors: {', '.join(self.authors)}\n"
            f"PDF: {self.pdf_url}\n"
        )