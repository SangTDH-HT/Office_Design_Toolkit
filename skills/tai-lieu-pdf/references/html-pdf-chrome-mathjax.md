---
name: pdf-tu-html-bang-chrome-mathjax
description: "Công thức tạo PDF có công thức toán trên máy này — Chrome headless + MathJax tex-svg tải về local"
---

> Nguồn: ghi nhớ `pdf-tu-html-bang-chrome-mathjax`, cập nhật 2026-09-17. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Máy này **không có** pandoc, wkhtmltopdf, pdflatex. Cách tạo PDF đẹp đã kiểm chứng:

1. Tải `https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js` (~2 MB) về cùng thư mục HTML, nhúng bằng `<script src="tex-svg.js">`. Dùng output **SVG** nên không phụ thuộc font toán — KaTeX thì phải kéo theo ~60 file woff2.
2. Viết HTML với `@page { size: A4 }`, `-webkit-print-color-adjust: exact` (nếu không màu nền hộp sẽ mất khi in).
3. `chrome.exe --headless --disable-gpu --no-sandbox --virtual-time-budget=90000 --print-to-pdf-no-header --print-to-pdf="<đường dẫn Windows>" <file.html>`. Không có `--virtual-time-budget` đủ lớn thì MathJax chưa render xong đã in.

**Font tiếng Việt:** stack `'Palatino Linotype','Cambria','Times New Roman',serif` + `'Segoe UI'` cho tiêu đề hiển thị đủ dấu — xem [google-fonts-thieu-dau-tieng-viet](font-tieng-viet.md) cho trường hợp web.

**Cập nhật 11/09/2026:** cờ bỏ header/footer giờ là `--no-pdf-header-footer`
(`--print-to-pdf-no-header` bị Chrome hiện tại lờ đi → PDF dính ngày giờ và URL).
URL phải là `file:///C:/Users/...` — đưa đường dẫn POSIX `/c/Users/...` vào là Chrome
in ra trang "Your file couldn't be accessed" mà vẫn exit 0. Kiểm ảnh ngay bằng
PyMuPDF (đã có: `import pymupdf; pg.get_pixmap(dpi=110).save(...)`) rồi Read PNG —
khỏi cần chụp screenshot HTML riêng. `\text{}` của MathJax SVG **mất dấu tiếng
Việt** (ra "x t d u c a"): chữ Việt để ngoài `$…$`, trong math chỉ giữ `\text{m}`.
CSS `.fig svg{width:100%}` bắt luôn SVG của MathJax → công thức phình cả trang;
dùng `.fig > svg`.

**Kiểm chứng không cần mở PDF** (hoặc dựng ảnh bằng PyMuPDF như trên):
- Đếm trang: đếm `/Type /Page` trong file nhị phân.
- Xác nhận MathJax đã chạy: giải nén stream bằng `zlib`, đếm `\lim`, `\dfrac`, `\int` — phải bằng 0. Còn LaTeX thô là MathJax hỏng.
- Kiểm tra dấu tiếng Việt và bố cục: dựng một file HTML trích đoạn rồi `chrome --headless --screenshot`, đọc PNG bằng Read tool.

**Ngắt trang (17/09/2026):** mẫu bài làm cũ để tiêu đề "Bài N" rơi lẻ cuối trang và cắt
đôi đề bài có hình. Thêm `h2,h3{break-after:avoid}` và `break-inside:avoid` cho khối
`.de` (đề + hình) — Chrome headless tôn trọng cả hai.

**Bẫy:** heredoc bash (`<<'EOF'`) chết với nội dung HTML/CSS dài — dùng Write tool ghi từng phần rồi `cat` ghép lại.
