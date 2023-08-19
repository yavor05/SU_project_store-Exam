    /* Because I didn't set placeholder values in forms.py they will be set here using vanilla Javascript
//We start indexing at one because CSRF_token is considered and input field
*/

    //Query All input fields
    var form_fields = document.getElementsByTagName('input')
    form_fields[1].placeholder = 'Username..';
    form_fields[2].placeholder = 'Email..';
    form_fields[3].placeholder = 'Enter password...';
    form_fields[4].placeholder = 'Confirm Password...';


    for (var field in form_fields) {
        form_fields[field].className += ' form-control'
    }
    function returnToHome() {
        // Redirect to the home page URL
        window.location.href = "{% url 'home_page' %}";
    }