var toggler = document.getElementsByClassName("caret");
var i;


function set_parent_ul_active(last_active_ul){
    console.log(`Entering function with ul ${last_active_ul.attr('id')}`);
    let caret = last_active_ul.siblings('span');
    caret.addClass('caret-down');
    if(last_active_ul.parents().find('ul.nested:not(.active)').length > 0)
    {
        let parent_ul = last_active_ul.parents().find('ul.nested:not(.active)');
        if(parseInt(last_active_ul.attr('id')) < parseInt(parent_ul.attr('id'))) return;
        parent_ul.addClass('active');
        console.log(`Parent of ul ${last_active_ul.attr('id')} is ul ${parent_ul.attr('id')}`);
        console.log(last_active_ul.parents().find('ul.nested:not(.active)'));
        set_parent_ul_active(parent_ul)
    }
    else{
        console.log(`Ended with ul ${last_active_ul.attr('id')}`)
        return;
    }
}
for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

let last_active_ul = $(".tree").find("ul.active").last();
console.log(`Started with ul ${last_active_ul.attr('id')}`)
set_parent_ul_active(last_active_ul);