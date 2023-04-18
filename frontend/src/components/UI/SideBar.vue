<template>
    <nav class="">
        <div class="z-[2000] fixed text-[22px] w-max top-0 left-0 h-full bg-slate-800 text-gray-100">
            <div>
                <div class="flex justify-center py-8 px-6 text-[28px] items-center ">
                    <IconsLogo class="mx-1 fill-gray-100"></IconsLogo>WikiNotes 2.0
                </div>
                <hr class="mx-1">
            </div>


            <div class="flex flex-col py-5 pl-8 space-y-2 ">
                <div>
                    <RouterLink to="/" class="flex items-center">
                        <IconsDashboard class="mr-2 fill-gray-100" />Dashboard
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/articles" class="flex items-center">
                        <IconsArticles class="mr-2 stroke-gray-100" />Articles
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/notes" class="flex items-center ">
                        <IconsNotes class="mr-2 stroke-gray-100" />Notes
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/chat" class="flex items-center ">
                        <IconsChat class="mr-2 stroke-gray-100" />Chat
                    </RouterLink>
                </div>
                <div class="absolute flex items-center bottom-16 ">
                    <IconsLogout class="mr-2 fill-gray-100" />Logout
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