function saveAction(actionBox) {
    // get the type and selector
    var actionId = actionBox.attr("id");
    var boxType = actionBox.find(".box-type").val();
    var boxSelector = actionBox.find(".selector").val();
    var parentActionId = actionBox.attr("parent_id");

    // TODO: save to database

}

function saveResult(resultBox) {
    // get the type and selector
    var resultId = resultBox.attr("id");
    var boxType = resultBox.find(".box-type").val();
    var boxSelector = resultBox.find(".selector").val();
    var actionId = resultBox.closest(".step").find(".box.action:first");

    // TODO: save to database
}

function attachRunListener() {
  $(".box.action .box-btn.run-box").click(function() {
    var actionId = $(this).closest(".box").attr("id");

    // TODO: API call
  });
}
