function confirmDelete(name) {
    if (confirm("Вы подтверждаете удаление " +name+ " ?")) {
        return true;
    } else {
        return false;
    }
}