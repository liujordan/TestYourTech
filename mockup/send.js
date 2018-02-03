function saveAction(box) {
    // get the type and selector
    var boxId = box.attr("id");
    var boxType = box.find(".box-type").val();
    var boxSelector = box.find(".selector").val();
    
    // save to database
    
}

function saveResult(box) {
    // get the type and selector
    var boxId = box.attr("id");
    var boxType = box.find(".box-type").val();
    var boxSelector = box.find(".selector").val();
    var actionId = box.closest(".step").find(".box.action:first");
    
    // save to database
}