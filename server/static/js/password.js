 $(function() {
        $('#submit').bind('click', function() {
          $.getJSON('/generate_pass', {
            a: $('input[value="special_char"]').val(),
            b: $('input[value="number"]').val()
          }, function(data) {
            $("#password_gen").text(data.password_to_return);
          });
          return false;
        });
      });