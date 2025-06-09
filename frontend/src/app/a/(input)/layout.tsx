"use client";

import Image from "next/image";
import style from "./layout.module.scss";
import Logo from "@/public/logo.png";

export default function DashboardLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className={style.account__div}>
            <div className={style.account__first_half}>
                <Image
                    src={Logo}
                    alt="not-found-logo"
                    className={style.notFound__logo}
                    height={200}
                />
            </div>

            <div className={style.account__second_half}>{children}</div>
        </div>
    );
}
