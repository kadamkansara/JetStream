$(document).ready(function() {
    // Example: Show an alert when a button is clicked
    $('#myButton').click(function() {
        alert('Button clicked!');
    });
    $('#myInput').on('keyup', function(){
        let filter = $(this).val().toUpperCase();
        $('#myTable tbody tr').filter(function() {
            var firstColumnText = $(this).find('td').first().text().toUpperCase(); // Get the text of the first column
            if (firstColumnText.indexOf(filter) > -1) { // Check if the first column contains the search value
                $(this).show(); // Show the row if it matches
            } else {
                $(this).hide(); // Hide the row if it does not match
            }
        });
        // if(filter.length > 2){
        //     let myTable = $('#myTable');
        //     let tr = document.getElemtsByTagName('tr');
    
        //     for(var i=0; i < tr.length; i++){
        //         let td = tr[i].getElementsByTagName('td')[0];
    
        //         if(td){
        //             let textvalue = td.textContent || td.innerHTML;
    
        //             if(textvalue.toUpperCase().indexOf(filter) > -1){
        //                 tr[1].style.display = "";
    
        //             }else{
        //                 tr[i].style.display = "none";
        //             }
        //         }
        //     }
        // }
    });
});