---
name: adobe-phong-cach
description: Cách Sáng làm việc với Adobe — Illustrator (MCP npx 66 tool, MCP Python, JSX qua COM), Photoshop (MCP photoshop, recipe xoá nền / xuất web / chỉnh màu); luật soát ảnh, toạ độ artboard, font tiếng Việt, cài đặt MCP. Dùng khi "mở Illustrator/Photoshop", "sửa file .ai/.psd", "xoá nền ảnh", "chỉnh ảnh", "xuất PNG/PDF từ Illustrator", "làm banner/bìa", "MCP illustrator lỗi", trước khi mở skill illustrator.
---

# Adobe theo kiểu Sáng

## Chọn đường

| Việc | Đi đường |
|---|---|
| Đọc/sửa tài liệu `.ai` đang mở, xuất PNG/PDF/SVG, soát trước in, trích token màu | MCP npx `illustrator-mcp-server` → skill [illustrator](../illustrator/SKILL.md) |
| Màu chữ, gradient có opacity, Pathfinder, z-order, dàn nhiều trang | JSX qua COM → skill [illustrator](../illustrator/SKILL.md) |
| Chạy ExtendScript tuỳ ý, chụp màn | MCP `illustrator` (Python, tool `run`/`view`) — `view` chụp **cả màn hình** và kéo Illustrator lên trước, tránh dùng khi Sáng đang làm việc |
| Ảnh: xoá nền, chỉnh màu, ghép, xuất nhiều cỡ | MCP `photoshop` → [photoshop-mcp](references/photoshop-mcp.md) |
| Tài liệu PDF nhiều trang không cần Illustrator | skill `tai-lieu-pdf` (HTML → PDF nhanh hơn, sửa dễ hơn) |

Cài đặt và bẫy cài: [illustrator-mcp-python](references/illustrator-mcp-python.md), cấu hình mẫu ở `mcp/` của repo.

## Luật chung

1. **Bám phiên đang mở**: `GetActiveObject("Illustrator.Application")` khi Illustrator đang chạy; `New-Object -ComObject` chỉ khi chưa chạy (và dọn tài liệu lỗi lần trước).
2. **Xuất PNG và nhìn trước khi nói xong.** Không lưu đè trước khi xem kết quả.
3. Artboard Illustrator **Y dương**: đọc `artboards[0].artboardRect` trước khi tính toạ độ, đổi `Y = H - yWeb`.
4. Font tiếng Việt: Arial, Segoe UI (`SegoeUI-Bold`, `SegoeUIBlack`) — **không Arial Black** (thiếu glyph Việt, Illustrator lặng lẽ thay font cho từng ký tự). Máy không có Montserrat.
5. File `.jsx` tiếng Việt sửa bằng Python đọc/ghi UTF-8, không `sed`/`perl -i`.
6. Tài liệu giao khách dựng bằng Illustrator: số liệu đọc từ nguồn thật (không lấy từ trí nhớ), ảnh đối chiếu giao diện thật trước khi viết bước, render từng trang PNG soát, chốt số phiên bản trên bìa và ghi một dòng lịch sử phiên bản.
