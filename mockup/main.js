// temp partials
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
                        <select class="type">\
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
                        <select class="type">\
                          <option value="element">Element</option>\
                          <option value="text">Text</option>\
                        </select>\
                        <input class="selector" type="text">\
                    </div>\
                </div>\
            </div>';

$(document).ready(function() {
    // result listener for initial action box
    resultBoxListener($(".box"));
    actionBoxListener($(".box"));
    trashListener($(".box"));
});

function resultBoxListener(aBox) {
    aBox.find(".box-btn.add-result").click(function() {
        $(this).closest(".step.col-md-3").append(resultBox);
        resultBoxListener($(".box.result:last"));
    });
}

function actionBoxListener(aBox) {
    aBox.find(".box-btn.next-action").click(function() {
        $(this).closest(".step.col-md-3").after(actionBox);
        actionBoxListener($(".box.action:last"));
        resultBoxListener($(".box.action:last"));
    });
}

function trashListener(aBox) {
    aBox.find(".box-btn.remove-box").click(function() {
       $(this).closest(".box").remove();
    });
}