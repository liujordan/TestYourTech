/**
 * This file is responsible for ensuring that the buttons work
 * for the flowchart when it is created.
 *
 */

// temp partials (to be refactored to be django partials)
var actionBox = '<div class="step col-md-3 rp"><div class="box action">\
                <div class="box-heading">\
                    <div class="box-title">\
                        Action\
                    </div>\
                    <div class="box-buttons">\
                        <div class="box-btn remove-box" style="font-weight:bold">\
                            <span class="fa fa-trash"></span>\
                        </div>\
                        <div class="box-btn add-result" style="font-weight:bold">\
                            <span class="fa fa-plus"></span>\
                        </div>\
                        <div class="box-btn next-action">\
                            <span class="fa fa-angle-right"></span>\
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
                          <option value="form">Form</option>\
                          <option value="click">Click</option>\
                        </select>\
                        <input class="selector" type="text">\
                    </div>\
                </div>\
            </div></div>';

var resultBox = '<div class="box result">\
                <div class="box-heading">\
                    <div class="box-title">\
                        Expected Result\
                    </div>\
                    <div class="box-buttons">\
                        <div class="box-btn add-result" style="font-weight:bold">\
                            <span class="fa fa-plus"></span>\
                        </div>\
                        <div class="box-btn remove-box" style="font-weight:bold">\
                            <span class="fa fa-trash"></span>\
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
                          <option value="element">Element</option>\
                          <option value="text">Text</option>\
                        </select>\
                        <input class="selector" type="text">\
                    </div>\
                </div>\
            </div>';

$(document).ready(function() {
    // button listeners for initial action boxes
    resultBoxListener($(".box"));
    actionBoxListener($(".box.action"));
    trashListener($(".box"));
    unfocusResultAutoSave($(".box.result"));
    unfocusActionAutoSave($(".box.action"));
});

// creating a new result box button listener
function resultBoxListener(aBox) {
    aBox.find(".box-btn.add-result").click(function() {
        $(this).closest(".step.col-md-3").append(resultBox);
        resultBoxListener($(this).closest(".step.col-md-3").find(".box.result:last"));
        trashListener($(this).closest(".step.col-md-3").find(".box.result:last"));
        unfocusResultAutoSave($(this).closest(".step.col-md-3").find(".box.result:last"));
    });
}

// create a new action box button listener
function actionBoxListener(aBox) {
    aBox.find(".box-btn.next-action").click(function() {
        $(this).closest(".step.col-md-3").after(actionBox);
        actionBoxListener($(".box.action:last"));
        resultBoxListener($(".box.action:last"));
        trashListener($(".box.action:last"));
        unfocusActionAutoSave($(".box.action:last"));
        $(this).hide();
    });
}

// removing a box button listener
function trashListener(aBox) {
    aBox.find(".box-btn.remove-box").click(function() {
        // result should be removed itself
        if ($(this).closest(".box").hasClass("result")) {
           $(this).closest(".box").remove();
        // all associated results should be deleted from an action
        } else if ($(this).closest(".box").hasClass("action")) {
            $(this).closest(".box").closest(".step").remove();
        }
    });
}

// each action box should have this listener attached to it - on unfocus,
// save that box to database
function unfocusActionAutoSave(actionBox) {
  actionBox.find(".selector").focusout(function() {
    saveAction(actionBox);
    console.log("action unfocus");
  });

  actionBox.find(".box-type").change(function() {
    saveResult(resultBox);
  });
}

function unfocusResultAutoSave(resultBox) {
  resultBox.find(".selector").focusout(function() {
    saveResult(resultBox);
  });

  resultBox.find(".box-type").change(function() {
    saveResult(resultBox);
  });
}
