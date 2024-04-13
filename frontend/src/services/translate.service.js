import axiosInstance from './axios'

function translate(message) {
    return axiosInstance
        .post(`translate`, {sentence: message})
        .then((response) => response.data)
        .catch((err)=> alert(err))
}
export default translate;