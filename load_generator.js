const axios = require('axios');
const _ = require('lodash');

BASE_URL = 'http://localhost:5000';

_.range(0, 100).forEach((i) => axios.get(`${BASE_URL}/long/`, {
  params: {
    order: i
  },
  timeout: 10000,
}).catch(rsp => console.log(rsp)));

