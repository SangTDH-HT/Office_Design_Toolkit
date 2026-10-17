---
name: khong-chiem-chuot-khi-thu-ui
description: "Thử giao diện (MES, app desktop) thì không giành chuột / không kéo cửa sổ lên trước — UIA Invoke + PrintWindow chụp nền"
---

> Nguồn: ghi nhớ `khong-chiem-chuot-khi-thu-ui`, cập nhật 2026-10-09. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Sáng 06/10/2026 (đang làm việc khác trên máy trong lúc em thử MES): "em có thể làm mà không chiếm chuột anh không?"

**Why:** bam_xy.ps1 / chon_don2.ps1 dùng SetCursorPos + PostMessage, len_truoc.ps1 + chup.ps1 (CopyFromScreen) phải kéo MES lên trước — giật chuột và cửa sổ của anh.

**How to apply:**
- Bấm: `uia.ps1 bam/tab/help` (InvokePattern / SelectionItemPattern), không SetCursorPos. Thẻ đơn (Border) không có UIA thì tránh bước đó hoặc hỏi trước.
- Chụp: PrintWindow(h, hdc, 2) — script chup_nen.ps1 (scratchpad phiên efecf1c4): chụp cửa sổ ở nền, chỉ cần cửa sổ không thu nhỏ.
- Đừng gọi len_truoc.ps1 / SetForegroundWindow.
Liên quan *mp-mes-vong-nghiem-thu*.

**07/10/2026 (MP MES, phiên "làm cho xong hết"):** Sáng hỏi giữa chừng "test chạy ngầm được không, đừng mở giao diện ?" → cả phiên chỉ chạy dòng lệnh (MSBuild, smoke, `MP.TroLyMcp.exe --hoi/--kiem`, `claude -p`, Chrome headless in PDF), không mở MES.
Em hiểu đây là ý muốn cho lúc anh đang dùng máy; chưa rõ có phải luật cho mọi phiên — việc buộc phải nhìn màn hình thì gom thành danh sách "chưa xem trên màn" thay vì tự mở.

**08/10/2026 (MP MES, hệ cảnh báo):** em mở MES bằng Start-Process hai lượt (cửa sổ nhảy lên trước); lượt hai cửa sổ đã ở dạng thu nhỏ ngay từ giây thứ 12 — em đoán anh tự thu nhỏ, anh không nói gì.
Cách không làm phiền, đã chạy được: **mở MES thu nhỏ, không lấy tiêu điểm** bằng `CreateProcess` với `STARTF_USESHOWWINDOW` + `wShowWindow = 7` (SW_SHOWMINNOACTIVE) — mẫu ở `C:\MinhPhuc\MP_MES\tools\kiem-thu-canh-bao\thu-tram.ps1`.
Cửa sổ thu nhỏ: UIA Invoke / Select và `IsOffscreen` vẫn đúng, đọc chữ được; PrintWindow chỉ ra 160×28 (không có ảnh). Popup `StaysOpen = false` không thử được khi MES không ở trước (tự đóng ngay) → ghi vào "chưa xem trên màn".
**How to apply:** bài thử chỉ cần chữ / SQL / log thì mở thu nhỏ kiểu này; cần ảnh thì dựng ngoài màn (ve-man.ps1, ve-canh-bao.ps1); buộc phải mở cửa sổ thật thì báo anh một câu trước mỗi lượt.

**10/10/2026 (MP MES, tab Dữ liệu):** cần ẢNH màn WPF mà không mở gì trên màn Sáng → PrintWindow trên desktop ẩn ra đen (DWM không vẽ).
Cách chạy được: tiến trình PowerShell `-STA` riêng trên desktop ẩn nạp `MP.MES.exe` (`Application.ResourceAssembly = mes`, `new App().InitializeComponent()`
lấy Theme), `AppConfig.Nap()`, đặt `Session.NguoiDung` bằng phản chiếu (DangNhap thật ghi config + thao tác), dựng chính lớp màn trong Window
`Left=-32000, ShowActivated=false`, bơm Dispatcher vài giây cho nạp xong, `RenderTargetBitmap` → PNG. Mẫu: `tools\kiem-thu-quan-ly\ve-tab-du-lieu.ps1`.
Lái chức năng thì vẫn MES thật trên desktop ẩn + UIA (`thu-tab-du-lieu.ps1`); UIA FindAll có lúc ném "Unrecognized error" khi cây đang dựng lại → thử lại.

**08/10/2026 21:25 (MP MES, phiên KẾT-NỐI):** Sáng tự mở NetToPLCsim rồi nhắn "em có thể mở phần mềm test thoải mái nhé". Em vẫn chạy MES trên **desktop ẩn** (`tools\kiem-thu-ket-noi\thu-mes.ps1`, CreateDesktop + UIA) — vừa không làm phiền vừa lái được hộp thoại; cửa sổ trước của anh không đổi suốt bài.
Đọc lời đó là cho phép của lượt này khi anh đã dựng PLCSIM, chưa phải bỏ luật "đừng giành màn".
