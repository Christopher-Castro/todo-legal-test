<template>
    <div>
        <Header/>
        Bien venido Usuario
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
export default {
  name: 'Dashboard',
  components: {
    Header,
    Footer
  }
}
</script>

<style scoped>

</style>
