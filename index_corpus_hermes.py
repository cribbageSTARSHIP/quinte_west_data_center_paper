import os
import json
import glob
import fitz  # PyMuPDF inside /opt/hermes/.venv

BASE_DIR = "/workspace"
INDEX_DIR = os.path.join(BASE_DIR, "raw_search_index")
os.makedirs(INDEX_DIR, exist_ok=True)

source_dirs = [
    ("primary_studies", os.path.join(BASE_DIR, "pdfs/data_center")),
    ("wiki_raw_papers_pdf", os.path.join(BASE_DIR, "wiki/raw/papers")),
    ("web_vault_pdfs", os.path.join(BASE_DIR, "wiki/raw/web_pdfs")),
]

total_pages = 0
indexed_files = 0
catalog = []

print("=== Indexing PDFs ===")
for category, s_dir in source_dirs:
    if not os.path.exists(s_dir):
        continue
    for pdf_path in sorted(glob.glob(os.path.join(s_dir, "*.pdf")) + glob.glob(os.path.join(s_dir, "*.PDF"))):
        filename = os.path.basename(pdf_path)
        try:
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                text = " ".join((doc[page_num].get_text() or "").split())
                if len(text) > 40:
                    catalog.append({
                        "category": category,
                        "filename": filename,
                        "path": pdf_path,
                        "page": page_num + 1,
                        "text": text
                    })
                    total_pages += 1
            doc.close()
            indexed_files += 1
        except Exception as e:
            print(f"Error {filename}: {e}")

print("=== Indexing Downstream Wiki Markdown & Articles ===")
md_dirs = [
    ("wiki_raw_papers", os.path.join(BASE_DIR, "wiki/raw/papers")),
    ("wiki_raw_articles", os.path.join(BASE_DIR, "wiki/raw/articles")),
    ("wiki_concepts", os.path.join(BASE_DIR, "wiki/concepts")),
    ("wiki_entities", os.path.join(BASE_DIR, "wiki/entities")),
]

for category, m_dir in md_dirs:
    if not os.path.exists(m_dir):
        continue
    for md_path in sorted(glob.glob(os.path.join(m_dir, "*.md"))):
        filename = os.path.basename(md_path)
        try:
            with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            chunk_size = 100
            for i in range(0, len(lines), chunk_size):
                chunk_text = " ".join("".join(lines[i:i+chunk_size]).split())
                if len(chunk_text) > 40:
                    catalog.append({
                        "category": category,
                        "filename": filename,
                        "path": md_path,
                        "page": f"lines_{i+1}-{i+len(lines[i:i+chunk_size])}",
                        "text": chunk_text
                    })
                    total_pages += 1
            indexed_files += 1
        except Exception as e:
            print(f"Error {filename}: {e}")

index_file = os.path.join(INDEX_DIR, "raw_corpus_index.json")
with open(index_file, "w", encoding="utf-8") as f:
    json.dump(catalog, f)

print(f"✓ Successfully indexed {indexed_files} source documents ({total_pages} pages/chunks) into {index_file}!")
