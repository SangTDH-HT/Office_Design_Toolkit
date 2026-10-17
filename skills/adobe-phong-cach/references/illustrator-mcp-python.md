---
name: illustrator-mcp-cai-dat
description: "MCP illustrator (krVatsal) ở C:\\Users\\Admin\\illustrator-mcp; cần pip install -e .; tool view chụp cả màn hình"
---

> Nguồn: ghi nhớ `illustrator-mcp-cai-dat`, cập nhật 2026-09-21. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

MCP `illustrator` (github.com/krVatsal/illustrator-mcp) cài ngày 21/09/2026 tại
`C:\Users\Admin\illustrator-mcp`, venv Python 3.12.10, đăng ký scope user trong `.claude.json`
(cùng chỗ `autocad-mcp`, `capcut`). Lệnh: `.venv\Scripts\python.exe -m illustrator`.

**Why:** hai chỗ không có trong README.
- README chỉ bảo `pip install -r requirements.txt`, nhưng khi đó `-m illustrator` chỉ chạy nếu cwd
  đúng thư mục repo. Claude Code spawn MCP với cwd là thư mục dự án đang mở → "No module named
  illustrator". Phải thêm `pip install -e .` vào venv.
- Tool `view` gọi `ImageGrab.grab()` → chụp **toàn màn hình**, không riêng cửa sổ Illustrator, và
  `AppActivate` kéo Illustrator lên trước nên cướp focus đang làm.

**How to apply:** Illustrator 2023 (COM Version 27.0.0) trả lời `Dispatch("Illustrator.Application")`
tốt; Dispatch tự khởi động Illustrator nếu chưa mở. Tool `run` chạy ExtendScript tuỳ ý — có File I/O
đầy đủ, coi như toàn quyền trên máy, đọc script trước khi chạy. Bản chạy được đã chạy
`pywin32_postinstall.py -install`.
