!function (t) { "use strict"; var o = function () { }; o.prototype.init = function () { t("#inline-editable").Tabledit({ inputClass: "form-control form-control-sm", editButton: !1, deleteButton: !1, columns: { identifier: [0, "id"], editable: [[2, "col2"], [3, "col3"]] } }), t("#btn-editable").Tabledit({ buttons: { edit: { class: "btn btn-success", html: '<span class="mdi mdi-pencil"></span>', action: "edit" } }, inputClass: "form-control form-control-sm", deleteButton: !1, saveButton: !1, autoFocus: !1, columns: { identifier: [[0, "id"], [1, "col1"]], editable: [[2, "col2"], [3, "col3"], [4, "col4"], [6, "col6"]] } }) }, t.EditableTable = new o, t.EditableTable.Constructor = o }(window.jQuery), function (t) { "use strict"; window.jQuery.EditableTable.init() }();