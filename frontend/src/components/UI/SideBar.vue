<template>
    <nav class="">
        <div class="fixed text-[22px] w-max top-0 left-0 h-full bg-pink-700 text-gray-100">
            <div>
                <div class="flex justify-center py-8 px-6 text-[28px] items-center ">
                    <IconsLogo class="fill-gray-100 mx-1"></IconsLogo>WikiNotes 2.0
                </div>
                <hr class="mx-1">
            </div>


            <div class=" pl-8 py-5 flex flex-col space-y-2">
                <div>
                    <RouterLink to="/dashboard" class="items-center flex">
                        <IconsDashboard class="fill-gray-100 mr-2" />Dashboard
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/articles" class="items-center flex">
                        <IconsArticles class="fill-gray-100 mr-2" />Articles
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/notes" class="items-center flex ">
                        <IconsNotes class="fill-gray-100 mr-2" />Notes
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/chat" class="items-center flex ">
                        <IconsChat class="fill-gray-100 mr-2" />Chat
                    </RouterLink>
                </div>
                <div class="absolute bottom-24 items-center flex ">
                    <IconsLogout class="fill-gray-100 mr-2" />Logout
                </div>
            </div>

        </div>
    </nav>
</template>
<script setup>
import IconsLogo from '../icons/IconsLogo.vue';
import IconsChat from '../icons/IconsChat.vue'
import IconsNotes from '../icons/IconsNotes.vue'
import IconsArticles from '../icons/IconsArticles.vue'
import IconsLogout from '../icons/IconsLogout.vue'
import IconsDashboard from '../icons/IconsDashboard.vue';

</script>

<script>
export default {
    name: "SideBar",
    components: { IconsDashboard }
}
</script>

<style scoped>
.router-link-active {
    transition: all 0.4s ease-out;
    background-color: rgba(240, 248, 255, 0.178);
    border-radius: 5px;
    padding-left: 10px;
    width: 200px
}
</style>