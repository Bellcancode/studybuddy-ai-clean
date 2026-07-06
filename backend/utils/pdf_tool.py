from .pdf_reader import extract_text_from_pdf


def read_pdf(pdf_path: str) -> str:
    """
    Reads a PDF and returns all extracted text.
    """
    return extract_text_from_pdf(pdf_path)