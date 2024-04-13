import axiosInstance from './axios'

function sendMessage(messages) {
    return axiosInstance
        .post(`chat`, messages)
        .then((response) => response.data)
        .catch((err) => alert(err))
}
export { sendMessage };