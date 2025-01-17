/**
 * This file is responsible for ensuring that the buttons work
 * for the flowchart when it is created.
 *
 */

// temp partials (to be refactored to be django partials)
var actionBox = '<div class="step col-md-3 rp"><div class="box action new">\
                <div class="box-heading">\
                    <div class="box-title">\
                        Action\
                    </div>\
                    <div class="box-buttons">\
                        <div class="box-btn remove-box" style="font-weight:bold">\
                            <span class="fa fa-trash"></span>\
                        </div>\
                        <div class="box-btn next-action">\
                            <span class="fa fa-plus"></span>\
                        </div>\
                    </div>\
                </div>\
                <div class="box-details">\
                    <div class="col-xs-4 rp">\
                        <span class="type-label">Type</span>\
                        <span class="selector-label">Selector</span>\
                    </div>\
                    <div class="col-xs-8 rp">\
                        <select class="box-type">\
                          <option value="">--Select One--</option>\
                          <option value="url">URL</option>\
                          <option value="type">Typing</option>\
                          <option value="click" selected="">Click</option>\
                        </select>\
                        <input class="selector" type="text">\
                    </div>\
                </div>\
            </div></div>';

$(document).ready(function() {
  // button listeners for initial action boxes
  actionBoxListener($(".box.action"));
  trashListener($(".box"));
  attachRunListener();
  $(".box").draggable({handle: ".box-heading"});

});

// create a new action box button listener
function actionBoxListener(box) {
  box.find(".box-btn.next-action").click(function() {
    // generate the html of the new actionbox
    var actionId = $(this).closest(".box").attr("id").split('-')[1];
    $.post('actions/',JSON.stringify({"name":"what"}), function(data, status) {
      alert("Data: " + data + "\nStatus: " + status);
      $.post(
        'action_link/',
        JSON.stringify({"this":actionId , "after":data['id']}),
        function(data, status){
          alert("Data: " + data + "\nStatus: " + status);
        });
    });
    $(this).closest(".step.col-md-3").after(actionBox);
    // attach all listeners to it
    actionBoxListener($(".box.action.new"));
    trashListener($(".box.action.new"));
    // make it draggable
    $(".box.action.new").draggable({handle: ".box-heading"});
    $(".box.action.new").removeClass("new");
  });
}

// removing a box button listener
function trashListener(aBox) {
  aBox.find(".box-btn.remove-box").click(function() {
    // result should be removed itself
    if ($(this).closest(".box").hasClass("action")) {
        $(this).closest(".box").closest(".step").remove();
    }
  });
}
$(".box").mouseup(function() {
  saveAction($(this));
});
