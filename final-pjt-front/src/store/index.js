import Vue from 'vue'
import Vuex from 'vuex'

import accounts from '@/store/modules/accounts'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts,
  }
})
