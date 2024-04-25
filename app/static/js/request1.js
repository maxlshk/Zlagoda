
document.addEventListener('alpine:init', () => {
    Alpine.data('request1',() => ({
        result: null,

        async sendRequest() {
            let baseUrl = window.location.origin;
            axios.get(`${baseUrl}/request1`)
                .then(response => {
                    this.result = response;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    createToast('error', `Error fetching data: ${error}`);
                });
        }

    }));
});