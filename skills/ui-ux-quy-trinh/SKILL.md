---
name: ui-ux-quy-trinh
description: Quy trình thiết kế giao diện Sáng đặt ra — gọi frontend-design trước dòng code đầu, lập bảng token 4–6 màu + font + wireframe ASCII, soát 5 kiểu "AI mặc định", soát UX bằng ui-ux-pro-max (tương phản, chỉ-màu, khoảng cách, trạng thái khoá), đồ thị qua dataviz; app WPF theo Theme.xaml, icon Lucide, co giãn theo màn; thử giao diện không chiếm chuột; đọc đúng lời chê/lệnh giao diện. Dùng khi dựng mới, sửa, "làm đẹp", "xấu quá", "căn chỉnh" bất kỳ trang web, HTML artifact, dashboard, form, app desktop WPF (MP MES), hoặc khi soát UX một giao diện trước khi giao.
---

# Quy trình UI/UX của Sáng

Luật gốc nằm trong `~/.claude/CLAUDE.md` của Sáng; skill này gom luật đó với những gì đã học được khi làm.

## Bốn bước bắt buộc (web, artifact, app desktop)

1. **Gọi Skill `frontend-design` trước dòng code đầu.** Nêu chủ đề, người dùng (thợ vận hành, kỹ sư, quản lý…) và việc chính của giao diện; brief chưa rõ thì hỏi lại. → [frontend-design-truoc](references/frontend-design-truoc.md)
2. **Bảng token ngắn**: 4–6 màu hex có tên, font và vai trò, wireframe ASCII, vài nguyên tắc.
3. **Soát bảng token với 5 kiểu "AI mặc định"** (nền kem + serif + đất nung; nền gần đen + một màu chua; kiểu báo kẻ chỉ mảnh góc vuông; bộ thẻ SaaS bo góc bóng xám; nhãn ALL-CAPS trên mọi tiêu đề, chuỗi "A · B · C", nhãn mono, mũi tên → trên nút). Trùng thì sửa, nói đã sửa gì, rồi mới code.
4. **Code xong tự phê bình**: bỏ bớt một thứ trang trí; kiểm responsive, focus bàn phím, `prefers-reduced-motion`.

## Soát UX bằng ui-ux-pro-max

Trước khi ghi giao diện vào project, tra bốn chủ đề và sửa theo:

```bash
python "C:/Users/Admin/.claude/skills/ui-ux-pro-max/scripts/search.py" "contrast" --domain ux -n 5
python "C:/Users/Admin/.claude/skills/ui-ux-pro-max/scripts/search.py" "color only" --domain ux -n 5
python "C:/Users/Admin/.claude/skills/ui-ux-pro-max/scripts/search.py" "touch target spacing" --domain ux -n 5
python "C:/Users/Admin/.claude/skills/ui-ux-pro-max/scripts/search.py" "disabled state" --domain ux -n 5
```

- Tính tương phản **từng cặp** chữ/nền: chữ thường ≥ 4,5:1 (đã bắt: `#9AA0A8` trên trắng chỉ 2,6:1).
- Trạng thái không chỉ phân biệt bằng màu — thêm icon, chữ, hình.
- Ô chọn/nút cạnh nhau cách ít nhất 8 px.
- Ô bị khoá phải trông bị khoá.
- Nói ngắn cho Sáng skill bắt được gì, đã sửa gì. → [soat-ux-pro-max](references/soat-ux-pro-max.md)

Bản cài toàn cục là v2.15.0 (18/10/2026); bản gốc lưu ở `vendor/ui-ux-pro-max-skill` kèm sáu skill anh em (banner-design, brand, design, design-system, slides, ui-styling).

## Thứ Sáng đã chê — không đề xuất lại

- Cửa sổ tự chế kiểu macOS (khung bạc gradient, ba nút tròn đỏ-vàng-xám, `WindowStyle=None`) đặt cạnh phần mềm có bộ mặt riêng.
- Hiệu ứng viền chạy / viền đổi màu làm thanh tiến trình cho hàng thẻ mốc.
- Thiết bị, icon tự ghép bằng hình tròn/chữ nhật khi đã có hình hoặc bộ icon sẵn.
- Muốn đổi kiểu khác những thứ trên thì hỏi ảnh mẫu trước, đừng tự chọn kiểu.

## App desktop WPF (MP MES)

- Dùng token có sẵn trong `Theme/Theme.xaml` (`Mau.*`, `Choi.*`, `CoChu.*`, `BoGoc.*`, `Phong.*`) và style trong `Theme/Controls.xaml`; không ghi mã màu thẳng; hộp thoại dùng khung cửa sổ Windows thường. → [app-wpf-theo-theme](references/app-wpf-theo-theme.md)
- Font giao diện tiếng Việt: Be Vietnam Pro (đủ 5 độ đậm, dấu cân).
- Icon: **Lucide** cho mọi giao diện (WPF sinh `Icons.xaml` bằng `lucide2xaml.py`).
- Màn trạm thật là 1280×1024 (vùng trang 1204×817, có dải cảnh báo 1204×764) — co giãn cả lưới một hệ số, soát 6 cỡ màn ra PNG. → [co-gian-theo-man](references/co-gian-theo-man.md)

## Đồ thị, đề xuất

Đồ thị nào cũng qua skill `dataviz` (bảng màu chạy validator); đề xuất cho người quyết luôn kèm bản HTML có đồ thị — khuôn ở skill `tai-lieu-pdf`.

## Thử và chụp không làm phiền Sáng

- Bấm bằng UIA Invoke/SelectionItem, không `SetCursorPos`, không kéo cửa sổ lên trước; mở app thu nhỏ không tiêu điểm (`SW_SHOWMINNOACTIVE`) hoặc chạy trên desktop ẩn. → [thu-ui-khong-chiem-chuot](references/thu-ui-khong-chiem-chuot.md)
- Ảnh WPF: dựng view ngoài màn + `RenderTargetBitmap`; **không bao giờ tạo `MP.Shell.App`** trong công cụ chụp (bật MES thật, có thể gửi lệnh PLC). → [chup-wpf-an-toan](references/chup-wpf-an-toan.md)
- Ảnh web: Chrome `--headless=new`; khổ 400 px thì bọc trang trong `<iframe style="width:400px">` rồi chụp cửa sổ 600 px; soát cả nền sáng và tối.

## Đọc lời Sáng về giao diện

- "chỉ cho hiện X thôi", "KHÔNG HIỆN CÁI NÀY" + ảnh = lệnh bỏ, không phải lời chê thiếu.
- Giọng Nam gõ nhanh: "giao" có thể là "dao".
- Hai ảnh mẫu + "hướng đầu tiên/cái này" → hỏi lại hoặc nói rõ đang hiểu là cái nào trước khi dựng. → [doc-lenh-giao-dien](references/doc-lenh-giao-dien.md)
