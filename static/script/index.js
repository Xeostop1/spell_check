//피드백: 벨류값 파라미터로 받기
function submitForm() {
  var text = $("#input_text").val();
  $.ajax({
    url: "/spell_check",
    type: "POST",
    contentType: "String",
    data: JSON.stringify({ text: text }),
    success: function (data) {
      try {
        $(".original").text(`입력 텍스트: ${text}`);
        // $(".corrected").text(`수정텍스트:${data.errata}`);
        $(".corrected").text(`수정텍스트:${data.correct_word}`);
      } catch (error) {
        console.error("접속불가 ajax:", error);
      }
    },
  });
}
