// Reply box popup JS
$(document).ready(function(){

    $('.reply-popup').click(function(e){
      commentId = (this.id); // or alert($(this).attr('id'));
      
     $('#rep_'+commentId).toggle();
    });

    // Check User is login or not
    $('#add-commentId').click(function(e){
      commenter = $('input[name=commenter]').val();
      if(commenter == ''){
      $('#modalSubscriptionForm').modal('show');
      }
    });
    
// $('#myModal').modal('toggle');
// $('#myModal').modal('show');
// $('#myModal').modal('hide');

// Post Comment
$('#commentBtn').click(function(){
  
  comment = $('#add-commentId').val();
  csrf = $('input[name=csrfmiddlewaretoken]').val();
  postId = $('input[name=postId]').val();
  $.ajax
  ({ 
    url: '/comments',
    data: {'comment': comment,'csrfmiddlewaretoken':csrf,'post_id':postId,'replyOn':0 },
    type: 'post',
    success: function(result)
    {
      if (result.code == 200){
      $('.errorClass1').empty();
      $('#exampleModalCenter').modal('show');
      }
      else{
      $('.errorClass1' ).html(result.message)
      }
    }
  });

});


// Check Is user logged or not before posting any reply to comment
$('.commentReply').click(function(){
    commenter = $('input[name=commenter]').val();
      if(commenter == ''){
      $('#modalSubscriptionForm').modal('show');
      }
      return null

});

// Comment reply message
$('.replybtn').click(function(){

  commenter = $('input[name=commenter]').val();
      if(commenter == ''){
      $('#modalSubscriptionForm').modal('show');
      return null
      }
  commentId = this.id
  comment = $('#replyComment_'+commentId).val();
  postId = $('input[name=postId]').val();
  csrf = $('input[name=csrfmiddlewaretoken]').val();

  if(comment == ''){
    return null
    }

   $.ajax
  ({ 
    url: '/comments',
    data: {'comment': comment,'csrfmiddlewaretoken':csrf,'post_id':postId,'replyOn':commentId },
    type: 'post',
    success: function(result)
    {
      if (result.code == 200){
      $('.errorClass1').empty();
      $('#exampleModalCenter').modal('show');
      }
      else{
      $('.errorClass1' ).html(result.message)
      }
    }
  });

});






$('.closeModel').click(function(){
  location.reload();

});


  });