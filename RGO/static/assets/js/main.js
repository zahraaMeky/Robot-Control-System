    
$(document).ready(function(){
 // Nice Scroll
    $("body").niceScroll({
        cursorcolor:"#B134A4",
        cursorwidth:"8px"
      });

    setInterval(function(){
      $.ajax({
        method:'GET',
        url: "getd", 
        success: function(response){
              var batt= ': ' + response.Batt + ' V';
              var temp= ': ' + response.temp + ' C';
              var pers= ': ' + response.pres + ' Bar';
              var con= ': ' + response.connected;
              var bat_rem= ': ' + response.Batt_lvl;
              var con_rem= ': ' + response.rem_connected;
              var Remote_connect = response.rem_connected;
              var Robot_connect = response.connected;
              $("#batt").html(batt);
              $("#temp").html(temp);
              $("#per").html(pers);
              $("#con").html(con);
              $("#bat-rem").html(bat_rem);
              $("#con-rem").html(con_rem);
               //check if robot connected and change style
               //if not connected change color to red
               if(Robot_connect == "disconnected"){
                $('#robotcon').removeClass('ifconnected');
                $('#robotcon').addClass('ifdisconnected');
              }else{
                $('#robotcon').removeClass('ifdisconnected');
                $('#robotcon').addClass('ifconnected');
              }
             
              //check if remote connected and change style
               //if not connected change color to red
              if(Remote_connect == "disconnected"){
                $('#remotecon').removeClass('ifconnected');
                $('#remotecon').addClass('ifdisconnected');
              }else{
                $('#remotecon').removeClass('ifdisconnected');
                $('#remotecon').addClass('ifconnected');
              }             
            console.log(response)    
    }});
  },800);

 // this function to change the main image 
 //when click on the thumbnails images 
  $(".img").on('click',function(){
    // Change src attribute of image
    $('#changeMe').attr('src', $(this).attr('src'));
    console.log($(this).attr('alt'));
    /*
    $.ajax({
        method:'GET',
        url: $(this).attr('alt'),
        success: function(response){
    }});
    */
}); 
});

