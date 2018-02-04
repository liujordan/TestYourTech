function saveAction(actionBox) {
    // get action related attributes
    var actionId = actionBox.attr("id").split("-")[1];
    var boxType = actionBox.find(".box-type").val();
    var boxSelector = actionBox.find(".selector").val();
    var boxTitle = actionBox.find(".box-title").val();
    var box_top = actionBox.css("top") || "0px";
    var box_left = actionBox.css("left") || "0px";

    // save action to database
    $.ajax({
      method: "POST",
      url: "/action/" + actionId + "/result/",
      data: { name: boxTitle, action_type: boxType, action_selector: boxSelector, left_pos: box_left, top_pos: box_top }
    })
      .done(function() {
        // TODO: want to edit the expected results as well
      });
}

function attachRunListener() {
  $(".box.action .box-btn.run-box").click(function() {
    var actionId = $(this).closest(".box").attr("id");
    $.post(
      'action/run_test/',
      {
        'action_id':actionId
      },
      function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      }
    );
  });
}
