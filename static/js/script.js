$("#transform").click(function(){
    let inputvalue = $("#inputarea").val();
    console.log(inputvalue);    
    $("#outputarea").text(inputvalue.split("").reverse().join(""));
    return false;
});
