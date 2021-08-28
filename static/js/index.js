$(document).ready(function() {
    let IPAddress = "Your PC's local IP here";
    let startvidURL = `http://${IPAddress}/youtube/startvid`;
    let actionURL = `http://${IPAddress}/youtube/player-action`;

    $("#play-video").click(function() {
        $.post(startvidURL, {"url" : $("#vidUrl").val()}, () => {});
        console.log("Posted")
    });
    $("#play-pause").click(function() {
        $.post(actionURL, {"action" : "play/pause"}, () => {});
        console.log("Posted")
    });
    $("#fullscreen").click(function() {
        $.post(actionURL, {"action" : "fullscreen"}, () => {});
        console.log("Posted")
    });
    $("#back10").click(function() {
        $.post(actionURL, {"action" : "back10"}, () => {});
        console.log("Posted")
    });
    $("#forward10").click(function() {
        $.post(actionURL, {"action" : "forward10"}, () => {});
        console.log("Posted")
    });
    $("#mute").click(function() {
        $.post(actionURL, {"action" : "mute"}, () => {});
        console.log("Posted")
    });
    $("#next").click(function() {
        $.post(actionURL, {"action" : "next"}, () => {});
        console.log("Posted")
    });
    $("#prev").click(function() {
        $.post(actionURL, {"action" : "previous"}, () => {});
        console.log("Posted")
    });
    $("#volplus").click(function() {
        $.post(actionURL, {"action" : "volume+"}, () => {});
        console.log("Posted")
    });
    $("#vol-").click(function() {
        $.post(actionURL, {"action" : "volume-"}, () => {});
        console.log("Posted")
    });
});