"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Cookies from "js-cookie";
import { verifyToken } from "@/services/api";

const HomePage = () => {
    const router = useRouter();

    useEffect(() => {
        const token = Cookies.get("token");

        if (!token) {
            router.push("/a");
            return;
        }

        const verify = async () => {
            try {
                const response = await verifyToken();
                router.push("/b");
            } catch (error) {
                console.error("Error verifying token:", error);
                Cookies.remove("token");
                router.push("/a");
            }
        };
        verify();
    }, [router]);

    return null; // You can return null as the page will handle the redirection
};

export default HomePage;
