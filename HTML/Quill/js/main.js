var quill = new Quill( "#example", {
  theme: "snow", // 模板
  modules: {
    toolbar: [
      // 工具列列表[註1]
      ['bold', 'italic', 'underline', 'strike'], // 粗體、斜體、底線和刪節線
      ['blockquote', 'code-block'], // 區塊、程式區塊
      [{ 'header': 1 }, { 'header': 2 }], // 標題1、標題2
      [{ 'list': 'ordered'}, { 'list': 'bullet' }], // 清單
      [{ 'script': 'sub'}, { 'script': 'super' }], // 上標、下標
      [{ 'indent': '-1'}, { 'indent': '+1' }], // 縮排
      [{ 'direction': 'rtl' }], // 文字方向
      [{ 'size': ['small', false, 'large', 'huge'] }], // 文字大小
      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],// 標題
      [{ 'color': [] }, { 'background': [] }], // 顏色
      [{ 'font': [] }], // 字體
      [{ 'align': [] }], // 文字方向
      [ 'clean' ] // 清除文字格是
    ]
  }
});