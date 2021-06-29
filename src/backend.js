import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers['X-API-KEY'] = token
  }
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {
  fetchToken () {
    return $axios.get(`/auth/uploadendpoint`)
      .then(response => response.data)
  },
  login (data) {
    return $axios.post(`/auth/login`, data)
  },
  register (data) {
    return $axios.post(`/auth/register`, data)
  },
  fetchTemplates () {
    return $axios.get(`/templates`)
  },
  fetchTemplate (id) {
    return $axios.get(`/template/${id}`)
  },
  createTemplate (data) {
    return $axios.post(`/templates`, data)
  },
  fetchListDatas (templateId) {
    return $axios.get(`/templates/${templateId}/list-datas`)
  },
  createDatas (templateId, data) {
    return $axios.post(`/templates/${templateId}/list-datas`, data)
  }
}
