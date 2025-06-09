import { useState } from "react";
import style from "./Navigation.module.scss";
import Link from "next/link";
import Image from "next/image";
import Logo from "@/public/logo.png";
import Cookies from "js-cookie";

const Navigation = () => {
    const [showMenu, setShowMenu] = useState(false);

    const toggleMenu = () => {
        setShowMenu((prev) => !prev);
    };

    return (
        <nav>
            <Image src={Logo} alt="logo" width={40}></Image>
            <div className={style.menu}>
                <Link href={"/f/"} className={style.menu__list}>
                    Feed
                </Link>
                <Link href={"/b/"} className={style.menu__list}>
                    Boards
                </Link>
            </div>
            <div className={style.account}>
                <i
                    className={`bi bi-person-circle`}
                    onClick={toggleMenu} // Toggle menu on click
                ></i>
                {showMenu && (
                    <div className={style.dropdown}>
                        <Link
                            href="/u"
                            className={style.dropdown__item}
                            onClick={() => setShowMenu(false)}
                        >
                            Profile
                        </Link>
                        <Link
                            href="/s"
                            className={style.dropdown__item}
                            onClick={() => setShowMenu(false)}
                        >
                            Settings
                        </Link>
                        <div
                            className={`${style.dropdown__logout} ${style.dropdown__item}`}
                            onClick={() => {
                                Cookies.remove("token");
                                window.location.href = "/a/";
                            }}
                        >
                            Logout
                        </div>
                    </div>
                )}
            </div>
        </nav>
    );
};

export default Navigation;
