        function view_enter(id)
        {
            document.getElementById(id).style.opacity= "1";
        }
        
        function view_out(id)
        {
            document.getElementById(id).style.opacity= ".2";
        }
        
        function when_click(id){
            var color = document.getElementById(id).style.backgroundColor;
            if(color != "red")
            {
                document.getElementById(id).style.backgroundColor="red";
            }
            else
            {
                document.getElementById(id).style.backgroundColor="buttonface"
            }
        }
        
