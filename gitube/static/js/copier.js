$(function(){
    var params = { wmode: "transparent" };
    var attributes = {};
    $('.git-addr').each(function(i){
        var self = $(this);
        self.after('<span id="copier'+ i +'"></span>');
        var flashvars = {};
        flashvars.s = self.text();
        swfobject.embedSWF("/static/copier.swf", "copier"+i, "16", "16", "9.0.0", 
                            false, flashvars, params, attributes);
    });
});
