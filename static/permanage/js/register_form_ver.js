function verify() {
    alert('11111');
    var firstname = document.getElementById('exampleFirstName').value;
    if (firstname == '') {
        alert('敢问阁下大名');
        return false;
    }
    var lastname = document.getElementById('exampleLastName').value;
    if (lastname == '') {
        alert('敢问阁下尊姓');
        return false;
    }
    var username = document.getElementById('exampleUserName').value;
    if (username == '') {
        alert('账号不能为空！');
        return false;
    }
    var passwd1 = document.getElementById('exampleInputPassword').value;
    var passwd2 = document.getElementById('exampleRepeatPassword').value;
    if (passwd1 != passwd2) {
        alert('两次密码输入不一致！');
        return false
    }
    if (passwd2 == '' || passwd1 == '') {
        alert('密码不能为空');
        return false;
    }
    if (passwd2.length < 6) {
        alert("密码的长度太短，应大于6");
        return false;
    }
    if (passwd2.length > 12) {
        alert("密码的长度太长，应该小于12");
        return false;
    }
    var email = document.getElementById('exampleInputEmail').value;
    return true;
}