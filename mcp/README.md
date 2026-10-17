# MCP cho Adobe

Cấu hình mẫu để dán vào `~/.claude.json` (hoặc `claude mcp add … --scope user`). Không file nào chứa khoá hay mật khẩu.

| Tên gợi ý | Dùng để | Cài | Cấu hình |
|---|---|---|---|
| `illustrator-ai` | 66 tool đọc/sửa tài liệu Illustrator đang mở, xuất PNG/PDF, soát in | `claude mcp add illustrator-ai --scope user -- npx -y illustrator-mcp-server` | [illustrator-npx.mcp.json](illustrator-npx.mcp.json) |
| `illustrator` | Chạy ExtendScript tuỳ ý (`run`), chụp màn (`view`) | clone `github.com/krVatsal/illustrator-mcp` vào `C:\Users\Admin\illustrator-mcp`, venv Python 3.12, `pip install -r requirements.txt` **và** `pip install -e .`, chạy `pywin32_postinstall.py -install` | [illustrator-python.mcp.json](illustrator-python.mcp.json) |
| `photoshop` | Sửa ảnh, recipe xoá nền / xuất web / màu | `npm i @alisaitteke/photoshop-mcp` vào một thư mục riêng, điền `PHOTOSHOP_PATH` | [photoshop.mcp.json](photoshop.mcp.json) |

Ghi chú:
- Gói npx phải đăng ký dưới tên khác `illustrator`, vì tên đó đã thuộc MCP Python. Skill `illustrator` gọi "MCP `illustrator`" là gói npx 66 tool.
- Cờ `-y` của `npx` là bắt buộc — thiếu thì `npx` hỏi "Ok to proceed?" và MCP treo im.
- Tool `view` của MCP Python chụp **cả màn hình** và kéo Illustrator lên trước — tránh khi Sáng đang làm việc.
- Bảng 66 tool và bẫy đã gặp: [skills/illustrator/mcp/README.md](../skills/illustrator/mcp/README.md).
