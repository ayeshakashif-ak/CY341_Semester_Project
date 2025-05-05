#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xfb738653, "filp_open" },
	{ 0x3971c70d, "crypto_alloc_ahash" },
	{ 0xe914e41e, "strcpy" },
	{ 0xf229424a, "preempt_count_add" },
	{ 0xdbb4464, "vmalloc_to_page" },
	{ 0x48d88a2c, "__SCT__preempt_schedule" },
	{ 0xc890c008, "zlib_deflateEnd" },
	{ 0x2b1a3924, "kernel_bind" },
	{ 0x8817df00, "param_ops_long" },
	{ 0x37a0cba, "kfree" },
	{ 0xb320cc0e, "sg_init_one" },
	{ 0x4302d0eb, "free_pages" },
	{ 0xae9532e0, "kernel_accept" },
	{ 0xf2c43f3f, "zlib_deflate" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0xda7220e7, "crypto_destroy_tfm" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0xd0da656b, "__stack_chk_fail" },
	{ 0xe9f7149c, "zlib_deflate_workspacesize" },
	{ 0x6a5cb5ee, "__get_free_pages" },
	{ 0x33b84f74, "copy_page" },
	{ 0x7cd8d75e, "page_offset_base" },
	{ 0x701ef4c6, "init_net" },
	{ 0x5a0b73d0, "zlib_deflateInit2" },
	{ 0x5268e6c, "kernel_sock_shutdown" },
	{ 0xd0760fc0, "kfree_sensitive" },
	{ 0x531b604e, "__virt_addr_valid" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x98794516, "current_task" },
	{ 0xb41a1101, "sock_set_reuseaddr" },
	{ 0x706c5a65, "preempt_count_sub" },
	{ 0x52a79ac6, "param_ops_charp" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xe892cf7c, "crypto_ahash_final" },
	{ 0xe2d5255a, "strcmp" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x97651e6c, "vmemmap_base" },
	{ 0x4629334c, "__preempt_count" },
	{ 0x47237e74, "kernel_listen" },
	{ 0xc0404ac4, "sock_create_kern" },
	{ 0x9daab73e, "filp_close" },
	{ 0x29c7f0ac, "sock_release" },
	{ 0xeaa1fdc0, "kmalloc_trace" },
	{ 0x754d539c, "strlen" },
	{ 0x77358855, "iomem_resource" },
	{ 0x7e662233, "param_ops_int" },
	{ 0xe30bb520, "kernel_sendmsg" },
	{ 0xf888ca21, "sg_init_table" },
	{ 0xc4f0da12, "ktime_get_with_offset" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0x4ca346e5, "kmalloc_caches" },
	{ 0xae285781, "kernel_write" },
	{ 0xb83992f2, "module_layout" },
};

MODULE_INFO(depends, "");

