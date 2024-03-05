document.getElementById('search').addEventListener('blur', function() {
    handleInput();
});

function handleInput() {
    document.getElementById('searchForm').submit();
}