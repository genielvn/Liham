"use client";

import Image from "next/image";
import style from "./page.module.scss";
import Logo from "@/public/logo.png";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Account() {
    const router = useRouter();

    return (
        <div className={style.account__div}>
            <div className={style.account__first_half}>
                <Image
                    src={Logo}
                    alt="logo"
                    className={style.notFound__logo}
                    height={200}
                />
            </div>

            <div className={style.account__second_half}>
                <div className={style.account__introduction}>
                    <h1>4uni</h1>
                    <p>Where students gather.</p>
                </div>
                <button
                    className="btn-full-width btn-hollow-pink margin-bottom-20"
                    onClick={() => router.push("/a/sign-in")}
                >
                    Sign In
                </button>
                <button
                    className="btn-full-width btn-solid-pink"
                    onClick={() => router.push("/a/sign-up")}
                >
                    Sign Up
                </button>
            </div>
        </div>
    );
}
