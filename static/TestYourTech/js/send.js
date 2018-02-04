function saveAction(actionBox) {
    // get action related attributes
    var actionId = actionBox.attr("id").split("-")[1];
    var boxType = actionBox.find(".box-type").val();
    var boxSelector = actionBox.find(".selector").val();
    var boxTitle = actionBox.find(".box-title").val();

    // save action to database
    $.ajax({
      method: "POST",
      url: "/action/" + actionId + "/result/",
      data: { name: boxTitle, action_type: boxType, action_selector: boxSelector }
    })
      .done(function() {
        // TODO: want to edit the expected results as well
      });
}

function attachRunListener() {
  $(".box.action .box-btn.run-box").click(function() {
    var actionId = $(this).closest(".box").attr("id");

    // TODO: API call to run the test case
  });
}
