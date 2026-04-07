import fitz  # PyMuPDF
import os
from PIL import Image


def parse_pdf(file):
    pdf_bytes = file.file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    chunks = []
    image_count = 0

    for page_num, page in enumerate(doc):
        # -------- TEXT --------
        text = page.get_text()
        if text.strip():
            chunks.append({
                "content": text,
                "type": "text",
                "page": page_num + 1
            })

        # -------- TABLE (basic handling as text for now) --------
        tables = page.get_text("blocks")
        for block in tables:
            if isinstance(block, tuple):
                table_text = block[4]
                if "|" in table_text or "\t" in table_text:
                    chunks.append({
                        "content": table_text,
                        "type": "table",
                        "page": page_num + 1
                    })

        # -------- IMAGES --------
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image_filename = f"image_page{page_num+1}_{img_index}.png"
            image_path = os.path.join("temp_images", image_filename)

            os.makedirs("temp_images", exist_ok=True)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            chunks.append({
                "content": image_path,
                "type": "image",
                "page": page_num + 1
            })

            image_count += 1

    return {
        "total_chunks": len(chunks),
        "images": image_count,
        "data": chunks
    }