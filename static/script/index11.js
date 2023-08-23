function submitForm() {
  alert("d");
  const text = $("#text").val();
  console.log(`입력한 텍스트: ${text}`);
  if (!isValidText(text)) {
    showModal();
    return false;
  }
}

$(document).ready(() => {
  $.ajax({
    url: "/spell_check",
    method: "POST",
    data: {
      text: text,
    },
    success: (data) => {
      try {
        console.log(`잘못된 단어 : ${data.wrong_words.join(", ")}`);
        console.log(`수정된 단어 : ${data.correct_words.join(", ")}`);
        $("#input-text").text("입력한 텍스트 :" + text);
        $("#original").text("잘못된 단어 :" + data.wrong_words.join(", "));
        $("#corrected").text("수정된 단어:" + data.correct_words.join(", "));
        return;
      } catch (error) {
        console.error("An error occurred:", error);
      }
    },
  });

  console.log("hell0");
  // 유효성 검사 함수

  // 모달창 열기 함수
  const showModal = () => {
    console.log("모달창 열기 함수 호출");
    $("#myModal").css("display", "block");
  };
  console.log("hell2");
  // 모달창 닫기 함수
  const closeModal = () => {
    console.log("모달창 닫기 함수 호출");
    $("#myModal").css("display", "none");
  };
  console.log("hell3");
  // // 폼 제출 함수

  // // 모달창 바깥 클릭 이벤트 처리 함수
  // $(window).click((event) => {
  //   const modal = $("#myModal");
  //   if (
  //     event.target == modal.get(0) ||
  //     $(event.target).hasClass("close-modal")
  //   ) {
  //     closeModal();
  //   }
  // });
});
