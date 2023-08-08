import axios from "axios";
const instance = axios.create({
    baseURL: "https://tirs.ai-lab.top/api/",
    // timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
});
export default instance
