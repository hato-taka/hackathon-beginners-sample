/*
各チャンネル詳細ページ内、ページ読み込み時に自動で下までスクロールする
*/

document.addEventListener("DOMContentLoaded", function () {
  const messageArea = document.getElementById("message-area");
  messageArea.scrollIntoView(false);
});
